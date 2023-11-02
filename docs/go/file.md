# phylosophy

first we collect the paths from the filesystem walk function
-> this allows to use the paths in a way that you can access the files concurrently

```golang
func (r *fsys) getPaths() error {
	if r.paths == nil {
		r.paths = []string{}
	}
	return fs.WalkDir(r.fs, ".", func(path string, d fs.DirEntry, err error) error {
		if err != nil {
			return err
		}
		if d.IsDir() {
			// Directory-based ignore rules should involve skipping the entire
			// contents of that directory.
			if r.rules.Ignore(path, d) {
				return filepath.SkipDir
			}
			return nil
		}
		if r.rules.Ignore(path, d) {
			return nil
		}
		r.paths = append(r.paths, path)
		return nil
	})
}
```

we access the files concurrently in a streaming or not

option 1: non streaming
option 2: streaming
- allows to provide checks -> protect size
- hash works like this with byte chunks

``` golang
func (r *fsys) load() (map[string]*bytes.Buffer, error) {
	var wg sync.WaitGroup
	files := newFiles()
	for _, path := range r.paths {
		path := path
		wg.Add(1)
		go func() {
			defer wg.Done()

			// option 1
			//b, err := os.ReadFile(path)

			// option 2
			// allows to provide checks
			// allows a hash + protect size
			f, err := r.fs.Open(path)
			if err != nil {
				// TODO see how to handle this error
				return
			}
			defer f.Close()

			// Create a buffer to read chunks of data
			buf := &bytes.Buffer{}
			buffer := make([]byte, 1024*1024)

			for {
				n, err := f.Read(buffer)
				if err != nil {
					if err == io.EOF {
						break
					}
					// TODO see how to handle this error
					fmt.Println("err", err)
					return
				}

				// Process and stream the data
				//fmt.Printf("File %s Read %d bytes: %s\n", path, n, string(buffer[:n]))
				buf.Write(buffer[:n])
			}
			files.add(path, buf)
		}()

	}
	wg.Wait()
	return files.get(), nil
}
```