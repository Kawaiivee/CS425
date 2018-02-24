REPORT=Report
for cmd in "$@"
do
    case $cmd in
	pdf)
	    echo "We will convert to pdf..."
	    pdflatex $REPORT.tex output-file=$REPORT.pdf
	     ;;
	
	     
	spell)
	    echo "Let's check the spelling"
	    aspell -t -c $REPORT.tex
	       ;;
	*) echo "remember to use 'pdf' or 'spell' or built your own";;
    esac
done
