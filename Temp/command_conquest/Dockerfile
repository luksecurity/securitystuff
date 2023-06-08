FROM php:7.4-apache

# Copy the web application files into the container
COPY index.php /var/www/html/index.php
COPY flag.txt /var/www/html/flag.txt

# Set permissions for the web application files
RUN chown -R www-data:www-data /var/www/html \
    && chmod -R 755 /var/www/html

# Enable Apache modules
RUN a2enmod rewrite

# Start the Apache service
CMD ["apache2-foreground"]

