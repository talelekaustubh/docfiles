# Use an official Golang image as the base image
FROM golang:1.20-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the go.mod file
COPY go.mod ./

# Download Go modules
RUN go mod download

# Copy the rest of the application code into the container
COPY . .

# Build the Go application
RUN go build -o goapp .

# Expose the port the app will run on
EXPOSE 8500

# Command to run the application
CMD ["./goapp"]
