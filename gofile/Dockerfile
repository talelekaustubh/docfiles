# Use Golang base image
FROM golang:1.19-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the Go application files
COPY . .

# Build the Go application
RUN go build -o goapp

# Expose the port
EXPOSE 8500

# Command to run the app
CMD ["./goapp"]