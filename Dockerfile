FROM nginx:alpine
# Copy your static files to the Nginx html directory
COPY . /usr/share/nginx/html
# Expose port 80
EXPOSE 80
