# Holdings Management/Alma Holdings Comparison Tool
This Docker image contains everything needed to compare the holdings in a CSV downloaded from EBSCOadmin's Holdings Management and an Excel .xls file resulting from the extended export of a portfolio list in Alma.

## Directions
1. Create the image with `docker build -t compare_holdings_image https://github.com/ereiskind/Compare_Holdings_Image.git#main`
2. Create a container based off the above image with `docker run --name Compare_Holdings --rm -dti compare_holdings_image`
3. Enter the container's bash shell with `docker exec -it Compare_Holdings /bin/bash`

* Exit the container's bash shell with `exit`
* Stop and destroy the container with `docker stop Compare_Holdings`