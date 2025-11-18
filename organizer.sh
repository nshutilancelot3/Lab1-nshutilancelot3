#!/bin/sh

dir_a="archive"
if [ ! -d "$dir_a" ]; then
    mkdir "$dir_a"
fi

csv_files=$(find . -maxdepth 1 -type f -name "*.csv")

log_file="organizer.log"

for csv_file in $csv_files; do
    bname=$(basename "$csv_file")

    timestamp=$(date +%Y%m%d-%H%M%S)

    name="${bname%.*}"
    extension="${bname##*.}"
    new_name="${name}-${timestamp}.${extension}"

    {
        echo "================Log Action==============="
        echo "Archived: $bname → $dir_a/$new_name"
        echo "Timestamp: $timestamp"
        echo "Content:"
        cat "$csv_file"
        echo "========================================="
    } >> "$log_files"

    mv "$csv_file" "$dir_a/$new_name"
done