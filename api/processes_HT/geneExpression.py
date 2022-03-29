def process_ge_to_jsont(tss):
    json_tss_table = {
        'comments': [],
        'columns': [],
        'data': []
    }
    columns = ['start', 'end', 'score', 'strand', 'sequence', 'genes']
    return json_tss_table


def process_ge_to_bedgraph(ge):
    # NC_000913.3 pl pr tpm  localhost:5000/ht/wdps/SRR10907670/ge/bedgraph
    # NC_000913.3	190	255	3780.619382
    header = 'track type=bedGraph name="BedGraph Format" description="BedGraph format" visibility=full color=200,100,0 altColor=0,100,200 priority=20'
    bedgraph_ge = ""
    for ex in ge:
        for key in ex:
            if not ex[key]:
                ex[key] = ""
        tuple_ts = (
            "NC_000913.3",
            str(ex['gene']['leftEndPosition']),
            str(ex['gene']['rightEndPosition']),
            str(ex['tpm'])
        )

        try:
            bedgraph_ge = bedgraph_ge+"\t".join(tuple_ts)+"\n"
        except Exception as e:
            print(e)
            print(ex)
    return header+"\n"+bedgraph_ge
