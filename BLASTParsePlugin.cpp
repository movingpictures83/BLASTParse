#include "PluginManager.h"
#include <stdio.h>
#include <stdlib.h>
#include "BLASTParsePlugin.h"

void BLASTParsePlugin::input(std::string file) {
 inputfile = file;
 std::ifstream ifile(inputfile.c_str(), std::ios::in);
 while (!ifile.eof()) {
   std::string key, value;
   ifile >> key;
   ifile >> value;
   parameters[key] = value;
 }
}

void BLASTParsePlugin::run() {

}

void BLASTParsePlugin::output(std::string file) {
   std::string command = "export OLDPATH=${PYTHONPATH}; ";
   command += "export PYTHONPATH=/usr/local/lib64/python3.9/site-packages/:${PYTHONPATH}; ";
   command += "python3.9 plugins/BLASTParse/runBLASTParse.py ";
   command += parameters["sqldatabase"] + " ";
   command += PluginManager::addPrefix(parameters["blastdatabase"]) + " ";
   command += parameters["pdbinput"] + " ";
   command += parameters["taxidfilter"] + " ";
   command += PluginManager::addPrefix(parameters["seqres"]) + " ";
   command += PluginManager::addPrefix(parameters["rasa"]) + " ";
   command += PluginManager::addPrefix(parameters["seqnums"]) + " ";
   command += PluginManager::addPrefix(parameters["seqsolv"]) + " ";
   command += file + "; ";
   command += "export PYTHONPATH=${OLDPATH}";
 std::cout << command << std::endl;

 system(command.c_str());
}

PluginProxy<BLASTParsePlugin> BLASTParsePluginProxy = PluginProxy<BLASTParsePlugin>("BLASTParse", PluginManager::getInstance());
