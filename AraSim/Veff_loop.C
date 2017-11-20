//Created by Jorge Torres, July 2017.
//Loops over AraSim output folders/files and prints the effective volume

void loop(const char *dirname="./",const char *ext)
{
  for(int j=0; j<1; j++){
    ext="AraOut";
    TSystemDirectory dir(dirname, dirname);
    TList *files = dir.GetListOfFiles();
    if (files) {
    TSystemFile *file;
    TString fname;
    TIter next(files);
    while ((file=(TSystemFile*)next())) {
      fname = file->GetName();
      if (!file->IsDirectory() && fname.BeginsWith(ext)) {
	TFile *AraOut = new TFile(fname.Data(),"READ");
	TTree *AraTree3 = (TTree*)AraOut->Get("AraTree3");
	double Veff;
	double entries;
	AraTree3->SetBranchAddress("VeffOmega", &Veff);
	entries= AraTree3->GetEntries();
	for (int i=0; i<entries; i++)
	  {
	    AraTree3->GetEntry(i);
	    //  
	  }
	std::cout <<  fname << "\t" <<  Veff << std::endl;
      }
    }
    }
  }
}

