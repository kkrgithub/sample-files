#renaming files in a sequence

a=1
for i in *.apk; do
  new=$(printf "%2d.apk" "$a") #04 pad to length of 4
  mv -- "$i" "$new"
  let a=a+1
done
