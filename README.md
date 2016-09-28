# Privacy crosstab reviews


## Useful Links
* [Home dir for notebooks] (http://data_privacy_review_box-c9-j9heiser.c9users.io/tree)
* [Generate new notebooks of crosstab reports] (http://data_privacy_review_box-c9-j9heiser.c9users.io/notebooks/Export_Privacy_Reviews.ipynb)


### Generating Reports
* start up the ipython notebook server by running this from the command line: `./notebooks/start_notebook.sh `    
* add the Json File of cross tab reports that you want to Run
* Your crosstab notebooks will be created. Take a look at them at where you specified in the json config files. 


### Important data security concepts to be aware of when using this tool

* QID-Quasi-identifier-is a set of attributes that could potentially identiy a record owner
* QID~ is an anonomous version of the original QID otained by applying anonmization operations to the attributes in the QID in the original table, D. 
* Record linkage attack- some value on the QID identifes a small number of records in the realeased table T, called a group. If the victim matches the value of ther QID, 
* the victim is vulnerable to being linked to the small number of records in the group. The attacher only faces a small number of possibilities for the victims record, and with the help of additional knowledge, there is a chance that the attacker could uniquely indentify the victim's record from the group.
* k-Anonymity- A defense against a record linkage attack- if one record in the table has some value QID, at least k-1 other records also have the value qid. The minimum group size on a QID is at least the value of k. 
* A table satifying this requirement is called k-anonymous. 
* k-Anonymous table - in this table, each record is indistinguishable from at least k-1 other records with respect to the QID. If this condition is satified, the probablily of the linking a victim to a specific record in the table throuhg QID is at most 1/k. 

 

