#!/bin/bash
clear

rah='\033[1;31m'
ngu='\033[1;35m'
ning='\033[1;33m'
ijo='\033[1;32m'
abu='\033[1;30m'
klat='\033[0;33m'
iru='\033[0;34m'
can='\033[1;36m'

echo $ning"       ╔════════╗"
echo "       ║        ║"
echo " ╔════════════════════╗"
echo " ║                    ║"$ngu" SIMPAN SCRIPT DI PALING LUAR SDCARD"
echo $ning" ║"$ijo"    ENCRYPT BASH"$ning"    ║"$ngu" MASUKAN SCRIPT ANDA DENGAN BENAR!"
echo $ning" ║                    ║" $ngu"CONTOH : [ script.sh ]"
echo $ning" ║                    ║" $ngu"FILE AKAN TERSIMPAN DI INTERNAL"
echo $ning" ╚════════════════════╝"


trap ctrl_c INT
ctrl_c() {
clear
cmatrix
sleep 1
exit
}
echo $rah"╔══════════════════════╗"
echo -n $abu" Nama script :"
read file
echo $rah"╚══════════════════════╝"
echo $rah"╔═══════════════════════════════════╗"
echo -n $abu" Nama hasil script encrypt :"
read output
echo $rah"╚═══════════════════════════════════╝"
bash-obfuscate /sdcard/$file -o /sdcard/$output
echo $ijo"[√]"$ngu"done"
echo ""
