# Holdings Management/Alma Holdings Comparison Tool
This Docker image contains everything needed to compare the holdings in a CSV downloaded from EBSCOadmin's Holdings Management and an Excel .xls file resulting from the extended export of a portfolio list in Alma.

## Directions
1. Create the image with `docker build -t compare_holdings_image https://github.com/ereiskind/Compare_Holdings_Image.git#main`
2. Create a container based off the above image with `docker run --name Compare_Holdings --rm -dti -p 3333:3333 compare_holdings_image`
3. Enter the container's bash shell with `docker exec -it Compare_Holdings bash`
4. Move to the OpenRefine folder with `cd openrefine-3.4.1`
5. Start OpenRefine with `./refine`
6. Go to http://127.0.0.1:3333/ to access OpenRefine in browser

*Note:* Opening OpenRefine switches the terminal to the program's own output; use ESC to return to bash