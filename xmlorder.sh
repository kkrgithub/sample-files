for i in range(1,5) ; do
   cd apktool/xml/"$i"
   mv AndroidManifest.xml "$i".xml
   cd -- 
done
