


```go
package main

import (
	"context"
	"fmt"
	"log"
	"net"

	"google.golang.org/grpc"
	pb "path/to/generated/kms/proto" // Replace with the actual path to your generated proto package
)

// KmsServer implements the KMS gRPC service
type KmsServer struct {
	pb.UnimplementedKeyManagementServiceServer
	encryptionKey []byte
}

// NewKmsServer creates a new KMS server instance
func NewKmsServer(key []byte) *KmsServer {
	return &KmsServer{encryptionKey: key}
}

// Encrypt encrypts the given plaintext
func (s *KmsServer) Encrypt(ctx context.Context, req *pb.EncryptRequest) (*pb.EncryptResponse, error) {
	// Example encryption using a simple XOR (replace with a proper encryption library)
	ciphertext := make([]byte, len(req.Plaintext))
	for i, b := range req.Plaintext {
		ciphertext[i] = b ^ s.encryptionKey[i%len(s.encryptionKey)]
	}

	return &pb.EncryptResponse{
		Ciphertext: ciphertext,
	}, nil
}

// Decrypt decrypts the given ciphertext
func (s *KmsServer) Decrypt(ctx context.Context, req *pb.DecryptRequest) (*pb.DecryptResponse, error) {
	// Example decryption using the same XOR (replace with a proper decryption library)
	plaintext := make([]byte, len(req.Ciphertext))
	for i, b := range req.Ciphertext {
		plaintext[i] = b ^ s.encryptionKey[i%len(s.encryptionKey)]
	}

	return &pb.DecryptResponse{
		Plaintext: plaintext,
	}, nil
}

// Status checks the health and version of the KMS server
func (s *KmsServer) Status(ctx context.Context, req *pb.StatusRequest) (*pb.StatusResponse, error) {
	return &pb.StatusResponse{
		Version: "v1.0",
		Healthz: "ok",
	}, nil
}

func main() {
	// Encryption key (replace with a secure key management system)
	encryptionKey := []byte("my-super-secret-key")

	// Create a new KMS server
	server := NewKmsServer(encryptionKey)

	// Set up gRPC server
	grpcServer := grpc.NewServer()
	pb.RegisterKeyManagementServiceServer(grpcServer, server)

	// Start listening
	listener, err := net.Listen("unix", "/tmp/kms.sock")
	if err != nil {
		log.Fatalf("Failed to listen on socket: %v", err)
	}
	fmt.Println("KMS server is running...")
	if err := grpcServer.Serve(listener); err != nil {
		log.Fatalf("Failed to serve gRPC server: %v", err)
	}
}
```

```go
import (
    "crypto/aes"
    "crypto/cipher"
    "crypto/rand"
    "io"
)

func encrypt(key, plaintext []byte) ([]byte, error) {
    block, err := aes.NewCipher(key)
    if err != nil {
        return nil, err
    }
    nonce := make([]byte, 12)
    if _, err := io.ReadFull(rand.Reader, nonce); err != nil {
        return nil, err
    }
    aesGCM, err := cipher.NewGCM(block)
    if err != nil {
        return nil, err
    }
    ciphertext := aesGCM.Seal(nil, nonce, plaintext, nil)
    return append(nonce, ciphertext...), nil
}

func decrypt(key, ciphertext []byte) ([]byte, error) {
    block, err := aes.NewCipher(key)
    if err != nil {
        return nil, err
    }
    aesGCM, err := cipher.NewGCM(block)
    if err != nil {
        return nil, err
    }
    nonce := ciphertext[:12]
    ciphertext = ciphertext[12:]
    return aesGCM.Open(nil, nonce, ciphertext, nil)
}
```


Enhancements

- Key Management
- Authenitcation and Authorization
- Logging and metrics
- Scalability