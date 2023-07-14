import to_bed_coordenates
import config

FILE_SNPS= 'list_snps.csv'
BED_SNPS = 'list_snps_bed.csv'




if __name__ == "__main__":
    
    FILE_POSITIONS= open.file(config.DATA_DIR/ FILE_SNPS, 'r')
    FILE_BED_POSITIONS=open.file(config.results / BED_SNPS, 'w')
    for position in FILE_POSITIONS:

        list_position=position.split(',')
        
        bed_position=to_bed_coordenates(list_position)
        print(bed_position)
