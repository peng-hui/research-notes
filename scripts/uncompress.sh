read -p 'Enter the directory path: ' directory
for sid in "$directory"/*; do
    for f in "$sid"/*; do
        if [ "${f: -4}" == ".rar" ]
        then
            unrar e "$f" -o+ "$sid" > /dev/null
        fi
        
        if [ "${f: -4}" == ".zip" ]
        then
            unzip -j -o -q "$f" -d "$sid"
        fi

        if [ "${f: -3}" == ".7z" ]
        then
            echo "$f"
            7z e "$f" -aoa -o"$sid" > /dev/null
        fi
    done
done
