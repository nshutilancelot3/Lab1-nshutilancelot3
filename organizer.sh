#!/bin/sh


log_file="organizer.log"
dir_a="archive"


log_csv_details() {
    local original_file="$1"
    local archived_name="$2"
    local ts="$3"
    
    {
        echo "================Log Action==============="
        echo "Archived: $original_file → $dir_a/$archived_name"
        echo "Timestamp: $ts"
        echo "Content:"
        cat "$original_file"
        echo "========================================="
    } >> "$log_file"
}


archive_csv() {
    local csv_file="$1"
    local bname=$(basename "$csv_file")
    local timestamp=$(date +%Y%m%d-%H%M%S)
    
    local name="${bname%.*}"
    local extension="${bname##*.}"
    local new_name="${name}-${timestamp}.${extension}"
    
    log_csv_details "$csv_file" "$new_name" "$timestamp"
    mv "$csv_file" "$dir_a/$new_name"
}



[ ! -d "$dir_a" ] && mkdir "$dir_a"

find . -maxdepth 1 -type f -name "*.csv" | while read -r csv_file; do
    archive_csv "$csv_file"
done