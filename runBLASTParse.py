from blastparser import BLASTParser
import sys

#SQLITE_DATABASE_DIR = "../../epitopedia.sqlite3"
#BLAST_DATABASE_DIR = "../../EPI_SEQ.fasta"
#PDB_INPUT="6VXX_A"
#taxid_filter=11118
#file_path = "query_pdb_seq.seqres.txt"
#rasa_path = open("query_pdb_seq.rasa.txt", 'r')
#seqnums_path = open("query_pdb_seq.seqnums.txt", 'r')
#seqsolv_path = open("query_pdb_seq.seqsolv.txt", 'r')
#OUTPUT_PREFIX="EPI_SEQ_hits"

SQLITE_DATABASE_DIR = sys.argv[1]
BLAST_DATABASE_DIR = sys.argv[2]
PDB_INPUT=sys.argv[3]
taxid_filter=sys.argv[4]
file_path = sys.argv[5]
rasa_path = open(sys.argv[6], 'r')
seqnums_path = open(sys.argv[7], 'r')
seqsolv_path = open(sys.argv[8], 'r')
OUTPUT_PREFIX=sys.argv[9]

print("BlASTing query protein against EPI-SEQ...")
def condInt(x):
    try:
        retval = int(x)
        return retval
    except:
        return x

def condFloat(x):
    try:
        retval = float(x)
        return retval
    except:
        return x


rasa = []
for line in rasa_path:
    line = line.strip()
    rasa.append(condFloat(line))

seqnums = []
for line in seqnums_path:
    line = line.strip()
    seqnums.append(condInt(line))

seqsolv = seqsolv_path.readline().strip()

bp = BLASTParser(
                        file_path,
                        PDB_INPUT,
                        BLAST_DATABASE_DIR,
                        acc_seq=rasa,
                        #taxids=args.taxid_filter,
                        taxids=taxid_filter,
                        pdb_seqnums=seqnums,
                        pdb_seqsolv=seqsolv,
)
hits = bp.gethits()
print("Query protein BLASTed against EPI-SEQ")
print(f"Number of unfiltered hits for {PDB_INPUT}: {len(hits)}")
hits.tocsv(f"{OUTPUT_PREFIX}_{PDB_INPUT}.tsv", SQLITE_DATABASE_DIR)
