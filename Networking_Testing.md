# Tests

## docker run --name Compare_Holdings --rm -dti -p 3333:3333 compare_holdings_image
* Container IP
* 127.0.0.1
* localhost
* host.docker.internal

## docker run --name Compare_Holdings --rm -dti --expose 3333 compare_holdings_image
* Container IP
* 127.0.0.1
* localhost
* host.docker.internal

## docker run --name Compare_Holdings --rm -dti -p 3333:3333 --expose 3333 compare_holdings_image
* Container IP
* 127.0.0.1
* localhost
* host.docker.internal

## docker run --name Compare_Holdings --rm -dti -p 3333:3333 --network="host" compare_holdings_image
* Container IP
* 127.0.0.1
* localhost
* host.docker.internal

## docker run --name Compare_Holdings --rm -dti --expose 3333 --network="host" compare_holdings_image
* Container IP
* 127.0.0.1
* localhost
* host.docker.internal

## docker run --name Compare_Holdings --rm -dti -p 3333:3333 --expose 3333 --network="host" compare_holdings_image
* Container IP
* 127.0.0.1
* localhost
* host.docker.internal

## docker run --name Compare_Holdings --rm -dti -p 3333:3333 --add-host="host.docker.internal:127.0.0.1" compare_holdings_image
* Container IP
* 127.0.0.1
* localhost
* host.docker.internal

## docker run --name Compare_Holdings --rm -dti --expose 3333 --add-host="host.docker.internal:127.0.0.1" compare_holdings_image
* Container IP
* 127.0.0.1
* localhost
* host.docker.internal

## docker run --name Compare_Holdings --rm -dti -p 3333:3333 --expose 3333 --add-host="host.docker.internal:127.0.0.1" compare_holdings_image
* Container IP
* 127.0.0.1
* localhost
* host.docker.internal

## docker run --name Compare_Holdings --rm -dti -p 3333:3333 --add-host="host.docker.internal:127.0.0.1" --add-host="gateway.docker.internal:127.0.0.1" compare_holdings_image
* Container IP
* 127.0.0.1
* localhost
* host.docker.internal

## docker run --name Compare_Holdings --rm -dti --expose 3333 --add-host="host.docker.internal:127.0.0.1" --add-host="gateway.docker.internal:127.0.0.1" compare_holdings_image
* Container IP
* 127.0.0.1
* localhost
* host.docker.internal

## docker run --name Compare_Holdings --rm -dti -p 3333:3333 --expose 3333 --add-host="host.docker.internal:127.0.0.1" --add-host="gateway.docker.internal:127.0.0.1" compare_holdings_image
* Container IP
* 127.0.0.1
* localhost
* host.docker.internal