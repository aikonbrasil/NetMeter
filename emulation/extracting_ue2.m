%% Import data from text file
% Script for importing data from the following text file:
%
%    filename: C:\Users\h18323\Documents\githubrepo\NetMeter\emulation\rf_field_info_02.csv
%
% Auto-generated by MATLAB on 18-Dec-2020 11:51:46

%% Setup the Import Options and import the data
opts = delimitedTextImportOptions("NumVariables", 8);

% Specify range and delimiter
opts.DataLines = [1, Inf];
opts.Delimiter = ",";

% Specify column names and types
opts.VariableNames = ["VarName1", "VarName2", "VarName3", "VarName4", "VarName5", "VarName6", "VarName7", "VarName8"];
opts.VariableTypes = ["double", "double", "double", "double", "double", "double", "datetime", "datetime"];

% Specify file level properties
opts.ExtraColumnsRule = "ignore";
opts.EmptyLineRule = "read";

% Specify variable properties
opts = setvaropts(opts, "VarName7", "InputFormat", "yyyy-MM-dd HH:mm:ss");
opts = setvaropts(opts, "VarName8", "InputFormat", "yyyy-MM-dd HH:mm:ss");

% Import the data
rffieldinfo02 = readtable("C:\Users\h18323\Documents\githubrepo\NetMeter\emulation\rf_field_info_05.csv", opts);


%% Clear temporary variables
clear opts

RSRP = rffieldinfo02.VarName3;
RSRQ = rffieldinfo02.VarName4;
RSSI = rffieldinfo02.VarName5;
SINR = rffieldinfo02.VarName6;

save('infoue5','RSRP', 'RSRQ', 'RSSI', 'SINR' )