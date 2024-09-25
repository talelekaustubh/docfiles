# Use the official OpenJDK image as the base image
FROM openjdk:17-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the jar file from the target directory
COPY target/java-docker-app-1.0-SNAPSHOT-jar-with-dependencies.jar app.jar

# Expose the port the app runs on
EXPOSE 7500

# Command to run the application
CMD ["java", "-jar", "app.jar"]
