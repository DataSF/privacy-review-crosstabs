# Privacy Crosstab Generator Tool
---
## Useful Links
* [Home dir for notebooks](http://data_privacy_review_box-c9-j9heiser.c9users.io/tree)
* [Generate new notebooks of crosstab reports](http://data_privacy_review_box-c9-j9heiser.c9users.io/notebooks/Export_Privacy_Reviews.ipynb)
---
## Purpose of this Tool
* The purpose of this is to generate crosstabs to evaluate if current transformations are aquadely protecting privacy as outlined in the Datasf privacy tool kit. 
* Using crosstabs is a way to identify groups of individuals that maybe susceptible to a data privacy attack. 
---
## Generating Reports
1. Start up the ipython notebook server by running this from the command line: 
```
./notebooks/start_notebook.sh
```
2. Upload the json config files of crosstab notebooks that you want to run 
3. Go to the [Generate new notebooks of crosstab reports](http://data_privacy_review_box-c9-j9heiser.c9users.io/notebooks/Export_Privacy_Reviews.ipynb) page
4. Specify the directory where your main config file lives (aka-main_config.json)
5. Your crosstab notebooks will be created. Click on the links to view. 
6. Once you've generated your crosstab notebooks, you will need to click through them to view the results.
7. Save the ipython notebook output by clicking on file save icon in the upper left. 

## Creating Config Files To Generate Reports
* You can generate numerious crosstabs at once. You will use json config files to this.

## Types of Config Files
### **main_config.json**:  contains a list of the config files that you want to use to generate crosstab notebooks.  

  * **main_config.json object keys**: 
    * **configFileN**: filepath -> the file path to your config file
    
    * The key, value pairs look something like this:
  ```
  "configFile1": "/full/path/to/filename_yr_json_configFile.json"
  ```
  * For each config file you that want to add, use the field name, "configFile1", "configFile2", etc
  
### **filename_yr_json_configFile.json**: contains your configs to generate crosstab notebooks
* Important to note, this file contains a list of items. Each item is defined by they key, `crosstab_notebook`
* Each `crosstab_notebook` list object will generate an ipython notebook. 
* Inside each `crosstab_notebook` list object, you will need to define several key, value pairs to generate a notebook. 

#### crosstab_notebook list object keys:

* **source_data_directory**: the directory path to the source data; aka the directory where the source data for the crosstabs is
* **output_notebook_base_directory**: full path of the base directory to where you want to output the generated notebook to
* **output_notebook_directory**: the sub folder of the output notebook base directory where you want to output the generated notebook to
* **output_notebook_filename**: the filename for the generated notebook
* **notebook_base_url**: the base url of the ipython notebook server where you want to display the generated crosstab notebook
* **crosstab_reports**: a dictionary that contains th
  *  **field_combo**: the fields you want to run a crosstab report on
  *  **k_annon_size**: minumum value a crosstab cell can contain.  
   
---

## Important data security concepts to be aware of when using this tool

#### General Terms
* QID-Quasi-identifier-is a set of attributes that could potentially identiy a record owner
* QID~ is an anonomous version of the original QID otained by applying anonmization operations to the attributes in the QID in the original table, D. 

#### Types of Linkage Attacks
* Record linkage attack- some value on the QID identifes a small number of records in the realeased table T, called a group. If the victim matches the value of ther QID, 
* the victim is vulnerable to being linked to the small number of records in the group. The attacher only faces a small number of possibilities for the victims record, and with the help of additional knowledge, there is a chance that the attacker could uniquely indentify the victim's record from the group.
* k-Anonymity- A defense against a record linkage attack- if one record in the table has some value QID, at least k-1 other records also have the value qid. The minimum group size on a QID is at least the value of k. 
* A table satifying this requirement is called k-anonymous. 
* k-Anonymous table - in this table, each record is indistinguishable from at least k-1 other records with respect to the QID. If this condition is satified, the probablily of the linking a victim to a specific record in the table throuhg QID is at most 1/k. 

 

