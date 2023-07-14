import to_bed_coordenates
import config
import subprocess

FILE_SNPS= 'test_snps.csv'
BED_SNPS = 'test_snps_bed.csv'

## escribe la orden bien, pero hay algo mal en la config de los ficheros y dice uque no los encuentra. Si la copias y vas a terminal funciona

## no pilla la primera linea del bed, hay que poner un head. Lo recupere a mano


if __name__ == "__main__":
    
    FILE_POSITIONS= open(config.DATA_DIR/ FILE_SNPS, 'r')
    FILE_BED_POSITIONS=open(config.DATA_RESULTS / BED_SNPS, 'w')
    for position in FILE_POSITIONS:

        SITE=position.replace('\n','').split(',')
        
       
        bed_position=to_bed_coordenates.change_coord_to_bed(chromosome=SITE[0],position=SITE[1])
        FILE_BED_POSITIONS.write(bed_position[0] +'\t'+ str(bed_position[1]) + '\t'+ str(bed_position[2]) + '\n')
    BED_FILE=open(config.DATA_RESULTS / BED_SNPS, 'r')
    COMMAND='vcftools --gzvcf ' + config.VCF_FILE + ' --recode --recode-INFO-all  --bed ' + \
    BED_FILE.name +  ' --stdout '

    CMD = ['bash', COMMAND]
    process = subprocess.run(CMD, check=True, stdout=subprocess.PIPE, universal_newlines=True)
   
    print(COMMAND)
FILE_POSITIONS.close()
FILE_POSITIONS.close() 
