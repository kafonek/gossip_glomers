## Test

Make sure to add a shebang to the top of the solution files, and that they are executable (`chmod +x`)

From this directory, assuming `maelstrom` is installed 
 1. ```
    ./maelstrom test -w echo \
      --bin solutions/01_echo.py \
      --time-limit 10 \
      --node-count 1
    ```
 2. ```
    ./maelstrom test -w unique-ids \
      --bin solutions/02_unique_id_generation.py \
      --time-limit 30 \
      --rate 1000 \
      --node-count 3 \
      --availability total \
      --nemesis partition
    ```