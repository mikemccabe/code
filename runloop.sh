
# Say you need to rename a bunch of image files
# not tested...

# cd dir_with_images
# mkdir renamed
# cd renamed

# I=100000 # this number should be big - it's to get 'zero padding'
# for ORIG_NAME in ls ../*.jpg; do
#     echo $ORIG_NAME;
#     NEW_NAME=p${I}.jpg;
#     cp $ORIG_NAME $NEW_NAME;
#     I=`expr $I + 1`;
# done


# run cmd for 0 .. $LIMIT inclusive, for LIMIT + 1 total calls

STARTXML=start.xml
ENDXML=end.xml
CURRENT_XML=current.xml
LIMIT=1000

# let's say you have 3000 images... in HDR groups of 3.
PIX_PER_HDRGROUP=3


I=0
while test $I -le $LIMIT; do
    # make new xml file
    echo $I
    python interpolate_xml.py $STARTXML $ENDXML $LIMIT $I > $CURRENT_XML
    
    INPUT_PICNO_0=`expr $I \* PIX_PER_HDRGROUP`
    INPUT_PICNO_1=`expr $INPUT_PICNO_0 + 1`
    INPUT_PICNO_2=`expr $INPUT_PICNO_0 + 2`

    # call yr thinger
    arseome_hdr_combiner --configfile=$CURRENT_XML --outfile=out${I}.jpg $INPUT_PICNO_0 $INPUT_PICNO_1 $INPUT_PICNO_2 > log$INPUT_PICNO_0

    I=`expr $I + 1`;
done

