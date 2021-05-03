read -p 'Enter the directory path: ' directory
for sid in "$directory"/*; do
    for f in "$sid"/*; do
        if [ "${f: -4}" == ".rar" ]
        then
            unrar e "$f" "$sid"
        fi
        
        if [ "${f: -4}" == ".zip" ]
        then
            unzip -j -o -q "$f" -d "$sid"
        fi
    done
done
