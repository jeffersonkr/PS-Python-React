# Use a node 14 image as the base
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Install npm
RUN apt-get update && apt-get install -y npm

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the required npm packages
RUN npm install

# Copy the rest of the files to the container
COPY . .

# Expose the container's network port
EXPOSE 3000

# Set the command to start the React app
CMD [ "npm", "start" ]
