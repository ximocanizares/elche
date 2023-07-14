
def change_coord_to_bed(chromosome, position):
    bed_coord = [chromosome, int(position)-1, int(position)]
    return(bed_coord)

if __name__ == "__main__":

    SITE=['ch4',123]

    print(change_coord_to_bed(chromosome=SITE[0],position=SITE[1] ))
