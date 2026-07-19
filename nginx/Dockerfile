# Use an official Nginx image as a base
FROM nginx:1.21.3-alpine

# Remove default config
RUN rm /etc/nginx/conf.d/default.conf

# Copy the custom Nginx configuration file into the container
COPY ./default.conf /etc/nginx/conf.d/