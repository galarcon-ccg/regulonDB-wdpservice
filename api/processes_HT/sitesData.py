def process_sites_to_jsonT(sites):
    json_sites_table = {
        'comments': [],
        'columns': [],
        'data': []
    }
    return json_sites_table

#NC_000913.3	RegulonDB	binding_site	8108	8130	5.4	-	.	name=tfbs in peak_3;sequence=CGAGACTGTTTCGGATTTCTGA
#chromosome,RegulonDB,binding_site,chrLeftPosition,chrRightPosition,score,strand,.,name="tfbs in peak 3";sequence=CGAT
def process_sites_to_gff3(sites):
    gff3_sites = """
    #chromosome,RegulonDB,binding_site,chrLeftPosition,chrRightPosition,score,strand,.,name="tfbs in peak 3";sequence=CGAT
    """
    return gff3_sites