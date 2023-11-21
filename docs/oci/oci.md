# oci specification

[RFC 6838]()
[RFC 5226]()

[oci runtime spec]()
[oci distribution spec]()
[oci artifacts](https://github.com/opencontainers/artifacts)


MediaTypeDescriptor     = "application/vnd.oci.descriptor.v1+json"
MediaTypeLayoutHeader   = "application/vnd.oci.layout.header.v1+json"
MediaTypeImageIndex     = "application/vnd.oci.image.index.v1+json"
MediaTypeImageManifest  = "application/vnd.oci.image.manifest.v1+json"
MediaTypeImageConfig    = "application/vnd.oci.image.config.v1+json"
MediaTypeEmptyJSON      = "application/vnd.oci.empty.v1+json"

MediaTypeImageLayer     = "application/vnd.oci.image.layer.v1.tar"
MediaTypeImageLayerGzip = "application/vnd.oci.image.layer.v1.tar+gzip"
MediaTypeImageLayerZstd = "application/vnd.oci.image.layer.v1.tar+zstd"


AnnotationCreated           = "org.opencontainers.image.created"
AnnotationAuthors           = "org.opencontainers.image.authors"
AnnotationURL               = "org.opencontainers.image.url"
AnnotationDocumentation     = "org.opencontainers.image.documentation"
AnnotationSource            = "org.opencontainers.image.source"
AnnotationVersion           = "org.opencontainers.image.version"
AnnotationRevision          = "org.opencontainers.image.revision"
AnnotationVendor            = "org.opencontainers.image.vendor"
AnnotationLicenses          = "org.opencontainers.image.licenses"
AnnotationRefName           = "org.opencontainers.image.ref.name"
AnnotationTitle             = "org.opencontainers.image.title"
AnnotationDescription       = "org.opencontainers.image.description"
AnnotationBaseImageDigest   = "org.opencontainers.image.base.digest"
AnnotationBaseImageName     = "org.opencontainers.image.base.name"

index:

``` golang
type Index struct {
    schemaVersion   int
    mediaType       string //`application/vnd.oci.image.index.v1+json`
    artifactType    string // IANA media type
    manifests       []Descriptor
    subject         *Descriptor
    annotations     map[string]string
}  
```

manifest:

``` golang
type Manifest struct {
    schemaVersion   int
    mediaType       string //`application/vnd.oci.image.manifest.v1+json`
    artifactType    string // IANA media type
    config          Descriptor
    layers         []Descriptor
    subject         *Descriptor
    annotations     map[string]string
}  
```

descriptor:

```golang
type Descriptor struct {
    mediaType       string
    digest          digest.Digest
    size            int64
    urls            []string
    annotations     map[string]string
    data            []byte
    platform        *Platform
    artifactType    string // IANA media type
}

type Platform struct {
    architecture    string // amd64, ppc641e, etc
    os              string // linux, windows
    os.version      string // `10.0.14393.1066
    os.features     []string 
    variant         string // example `v7` to specify ARMv7 when architecture is `arm`
}
```

image

```golang
type Image struct {
    created         *time.Time
    author          string
    Platform
    config          ImageConfig
    rootfs          RootFs
    history         []History
}

type ImageConfig struct {
    User            string
    ExposedPorts    map[string]struct{}
    Env             []string
    Entrypoint      []string
    Cmd             []string
    Volumes         map[string]struct{}
    WorkingDir      string
    Labels          map[string]string
    StopSignal      string
    ArgsEscaped     bool
}

type RootFS struct {
    type string
    diff_ids []digest.Digest
}

type History struct {
    created         *time.Time
    createdBy       string
    author          string
    comment         string
    empty_layer     bool
}
```

layout

```golang
type Layout struct {
    imageLayoutVersion string
}
```