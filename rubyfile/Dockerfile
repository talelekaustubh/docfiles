
# Use an official Ruby image as the base image
FROM ruby:3.2-alpine

# Install dependencies
RUN apk add --no-cache build-base

# Set the working directory in the container
WORKDIR /app

# Copy the Gemfile and install gems
COPY Gemfile ./
RUN bundle install

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app will run on
EXPOSE 5500

# Command to run the Ruby application
CMD ["ruby", "app.rb"]
