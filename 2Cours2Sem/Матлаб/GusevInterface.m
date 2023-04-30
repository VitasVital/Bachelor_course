function varargout = GusevInterface(varargin)
% GUSEVINTERFACE MATLAB code for GusevInterface.fig
%      GUSEVINTERFACE, by itself, creates a new GUSEVINTERFACE or raises the existing
%      singleton*.
%
%      H = GUSEVINTERFACE returns the handle to a new GUSEVINTERFACE or the handle to
%      the existing singleton*.
%
%      GUSEVINTERFACE('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in GUSEVINTERFACE.M with the given input arguments.
%
%      GUSEVINTERFACE('Property','Value',...) creates a new GUSEVINTERFACE or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before GusevInterface_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to GusevInterface_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help GusevInterface

% Last Modified by GUIDE v2.5 05-May-2020 13:43:31

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @GusevInterface_OpeningFcn, ...
                   'gui_OutputFcn',  @GusevInterface_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before GusevInterface is made visible.
function GusevInterface_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to GusevInterface (see VARARGIN)

% Choose default command line output for GusevInterface
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes GusevInterface wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = GusevInterface_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;

% --- Executes on button press in btnPlot1.
function btnPlot1_Callback(hObject, eventdata, handles)
% hObject    handle to btnPlot1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
x=-2:0.2:2;
y=exp(-x.^2);
plot(x,y)
set(hObject, 'Enable', 'off')
set(handles.btnPlot2, 'Enable', 'off')
set(handles.btnPlot3, 'Enable', 'off')
set(handles.btnClear, 'Enable', 'on')

% --- Executes on button press in btnClear.
function btnClear_Callback(hObject, eventdata, handles)
% hObject    handle to btnClear (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
cla
set(hObject, 'Enable', 'off')
set(handles.btnPlot1, 'Enable', 'on')
set(handles.btnPlot2, 'Enable', 'on')
set(handles.btnPlot3, 'Enable', 'on')


% --- Executes on button press in btnPlot2.
function btnPlot2_Callback(hObject, eventdata, handles)
% hObject    handle to btnPlot2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
x=-2:0.2:2;
y=exp(-x.^3);
plot(x,y)
set(hObject, 'Enable', 'off')
set(handles.btnPlot1, 'Enable', 'off')
set(handles.btnPlot3, 'Enable', 'off')
set(handles.btnClear, 'Enable', 'on')


% --- Executes on button press in btnPlot3.
function btnPlot3_Callback(hObject, eventdata, handles)
% hObject    handle to btnPlot3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
x=-2:0.2:2;
y=exp(-x.^4);
plot(x,y)
set(hObject, 'Enable', 'off')
set(handles.btnPlot1, 'Enable', 'off')
set(handles.btnPlot2, 'Enable', 'off')
set(handles.btnClear, 'Enable', 'on')
