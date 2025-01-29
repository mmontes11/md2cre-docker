# Use the official Ruby image from Docker Hub
FROM ruby:3.0

# Set the working directory inside the container
WORKDIR /usr/src/app

# Install the necessary gem
RUN gem install redcarpet

# Copy your Ruby script into the container
COPY md2cre.rb .

# Command to execute the Ruby script
ENTRYPOINT ["ruby", "md2cre.rb"]
