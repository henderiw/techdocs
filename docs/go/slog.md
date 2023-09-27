# slog

structured logging

introduced in go 1.21

[slog info](https://www.gopherguides.com/articles/golang-slog-package)

## basics

```go
package main

import "log/slog"

func main() {
	slog.Info("hello gophers")
	slog.Warn("be warned!")
	slog.Error("this is broken")
	slog.Debug("show some debugging output")
}
```

## logger

```go
package main

import (
	"log/slog"
	"os"
)

func main() {
	logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))
	logger.Info("hello gophers")
	logger.Warn("be warned!")
	logger.Error("this is broken")
}
```

## default logger


```go
package main

import (
	"log"
	"log/slog"
	"os"

	"training/store"
)

func main() {
	logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))
	logger.Info("hello gophers")
	logger.Warn("be warned!")
	logger.Error("this is broken")

	// Set the logger for the application -> any slog/log will use the default logger
	slog.SetDefault(logger)

	s := store.New()

	// we can now use the standard logger again as it uses the options we set above
	slog.Info("new store created", "store-id", s.ID)

	// the standard logger now uses the new logger as well
	log.Println("I'm log.println, look at me!")
}
```

## levels

```go
package main

import (
	"log/slog"
	"os"
)

func main() {
	// create a logging level variable
	// the level is Info by default
	var loggingLevel = new(slog.LevelVar)

	// Pass the loggingLevel to the new logger being created so we can change it later at any time
	logger := slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: loggingLevel}))

	// set the global logger
	slog.SetDefault(logger)
	// set the level to debug
	loggingLevel.Set(slog.LevelDebug)

	logger.Info("hello gophers")
	logger.Warn("be warned!")
	logger.Error("this is broken")
	logger.Debug("be warned!")
}
```

## grouping values

```go
package main

import (
	"log"
	"log/slog"
	"net/http"
	"os"
)

func main() {
	// create, configure, and set the global logger.
	var loggingLevel = new(slog.LevelVar)
	logger := slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: loggingLevel}))
	slog.SetDefault(logger)
	loggingLevel.Set(slog.LevelDebug)

	log.Println("program started")
	r, err := http.Get("https://www.gopherguides.com")
	if err != nil {
		slog.Error("error retrieving site", "err", err)
	}
	slog.Info("success", slog.Group("request", "method", r.Request.Method, "url", r.Request.URL.String()))

}
```

returns

```
{"time":"2023-08-10T10:55:18.368684-05:00","level":"INFO","msg":"program started"}
{"time":"2023-08-10T10:55:18.748639-05:00","level":"INFO","msg":"success","request":{"method":"GET","url":"https://www.gopherguides.com"}}

```

## improving performace

slog.Int, slog.String, slog.Bool and slog.Any

```go
package main

import (
	"log"
	"log/slog"
	"net/http"
	"os"
)

func main() {
	// create, configure, and set the global logger.
	var loggingLevel = new(slog.LevelVar)
	logger := slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: loggingLevel}))
	slog.SetDefault(logger)
	loggingLevel.Set(slog.LevelDebug)

	log.Println("program started")
	r, err := http.Get("https://www.gopherguides.com")
	if err != nil {
		slog.Error("error retrieving site", slog.String("err", err.Error()))
	}
	slog.Info("success",
		slog.Group(
			"request",
			slog.String("method", r.Request.Method),
			slog.String("url", r.Request.URL.String()),
		))
}
```

## customizing log behavior

## adding source file info

```go
package main

import (
	"log/slog"
	"os"
	"training/store"
)

func main() {
	logger := slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{AddSource: true}))
	// Set the logger for the application
	slog.SetDefault(logger)

	slog.Info("hello gophers")
	slog.Warn("be warned!")
	slog.Error("this is broken")

	_ = store.New()
}
```

update the default behavior

```go
package main

import (
	"log/slog"
	"os"
	"path/filepath"

	"training/store"
)

func main() {
	replacer := func(groups []string, a slog.Attr) slog.Attr {
		if a.Key == slog.SourceKey {
			source := a.Value.Any().(*slog.Source)
			source.File = filepath.Base(source.File)
		}
		return a
	}

	logger := slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{AddSource: true, ReplaceAttr: replacer}))
	// Set the logger for the application
	slog.SetDefault(logger)

	slog.Info("hello gophers")
	slog.Warn("be warned!")
	slog.Error("this is broken")

	_ = store.New()
}
```