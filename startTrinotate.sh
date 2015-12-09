cd ~/software/Trinotate-2.0.2/TrinotateWeb
module load perl
echo "browser site: http://bragg-gpu.hpc.csiro.au:8080/cgi-bin/index.cgi"
echo "data: /data/nea040/1.prawnRNAi/7.sqliteResults/Trinotate.sqlite"
./matt_run_mongoose_webserver.sh

