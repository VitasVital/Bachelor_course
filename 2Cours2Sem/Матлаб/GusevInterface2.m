function varargout = GusevInterface2(varargin)
% GUSEVINTERFACE2 MATLAB code for GusevInterface2.fig
%      GUSEVINTERFACE2, by itself, creates a new GUSEVINTERFACE2 or raises the existing
%      singleton*.
%
%      H = GUSEVINTERFACE2 returns the handle to a new GUSEVINTERFACE2 or the handle to
%      the existing singleton*.
%
%      GUSEVINTERFACE2('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in GUSEVINTERFACE2.M with the given input arguments.
%
%      GUSEVINTERFACE2('Property','Value',...) creates a new GUSEVINTERFACE2 or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before GusevInterface2_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to GusevInterface2_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help GusevInterface2

% Last Modified by GUIDE v2.5 14-May-2020 13:22:42

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @GusevInterface2_OpeningFcn, ...
                   'gui_OutputFcn',  @GusevInterface2_OutputFcn, ...
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


% --- Executes just before GusevInterface2 is made visible.
function GusevInterface2_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to GusevInterface2 (see VARARGIN)

% Choose default command line output for GusevInterface2
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes GusevInterface2 wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = GusevInterface2_OutputFcn(hObject, eventdata, handles) 
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
handles.Line=plot(x,y)
guidata(gcbo, handles)

set(hObject, 'Enable', 'off')
set(handles.btnPlot2, 'Enable', 'on')
set(handles.btnPlot3, 'Enable', 'on')
set(handles.btnPlot4, 'Enable', 'on')
set(handles.btnPlot5, 'Enable', 'on')
set(handles.btnClear, 'Enable', 'on')

set(handles.rbMarkCirc, 'Enable', 'on')
set(handles.rbMarkSq, 'Enable', 'on')
set(handles.rbMarkNone, 'Enable', 'on')
set(handles.rbMarkStar, 'Enable', 'on')
set(handles.rbMarkTriangle, 'Enable', 'on')
set(handles.rbMarkRhombus, 'Enable', 'on')

set(handles.pmColor, 'Enable', 'on')
set(handles.scrWidth, 'Enable', 'on')

if get(handles.chbxGridX, 'Value')
    set(gca,'XGrid', 'on')
else
    set(gca,'XGrid','off')
end
if get(handles.chbxGridY, 'Value')
    set(gca,'YGrid', 'on')
else
    set(gca,'YGrid','off')
end

if get(handles.rbMarkCirc, 'Value')
    set(handles.Line, 'Marker', 'o')
end
if get(handles.rbMarkSq, 'Value')
    set(handles.Line, 'Marker', 's')
end
if get(handles.rbMarkStar, 'Value')
    set(handles.Line, 'Marker', '*')
end
if get(handles.rbMarkTriangle, 'Value')
    set(handles.Line, 'Marker', '^')
end
if get(handles.rbMarkRhombus, 'Value')
    set(handles.Line, 'Marker', 'd')
end

if get(handles.rbMarkCirc, 'Value')
    set(handles.rbMarkCirc, 'Enable', 'inactive')
end
if get(handles.rbMarkSq, 'Value')
    set(handles.rbMarkSq, 'Enable', 'inactive')
end
if get(handles.rbMarkNone, 'Value')
    set(handles.rbMarkNone, 'Enable', 'inactive')
end
if get(handles.rbMarkStar, 'Value')
    set(handles.rbMarkStar, 'Enable', 'inactive')
end
if get(handles.rbMarkTriangle, 'Value')
    set(handles.rbMarkTriangle, 'Enable', 'inactive')
end
if get(handles.rbMarkRhombus, 'Value')
    set(handles.rbMarkRhombus, 'Enable', 'inactive')
end

Num=get(handles.pmColor, 'Value');
switch Num
    case 1
        set(handles.Line, 'Color', 'b')
    case 2
        set(handles.Line, 'Color', 'r')
    case 3
        set(handles.Line, 'Color', 'g')
    case 4
        set(handles.Line, 'Color', 'y')
    case 5
        set(handles.Line, 'Color', 'k')
    case 6
        set(handles.Line, 'Color', 'm')
    case 7
        set(handles.Line, 'Color', 'c')
end

width=get(handles.scrWidth, 'Value');
set(handles.Line, 'LineWidth', round(width))


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
set(handles.btnPlot4, 'Enable', 'on')
set(handles.btnPlot5, 'Enable', 'on')

set(handles.rbMarkCirc, 'Enable', 'off')
set(handles.rbMarkSq, 'Enable', 'off')
set(handles.rbMarkNone, 'Enable', 'off')
set(handles.rbMarkStar, 'Enable', 'off')
set(handles.rbMarkTriangle, 'Enable', 'off')
set(handles.rbMarkRhombus, 'Enable', 'off')

set(handles.pmColor, 'Enable', 'off')
set(handles.scrWidth, 'Enable', 'off')


% --- Executes on button press in btnPlot2.
function btnPlot2_Callback(hObject, eventdata, handles)
% hObject    handle to btnPlot2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
x=-2:0.2:2;
y=exp(-x.^3);
handles.Line=plot(x,y)
guidata(gcbo, handles)

set(hObject, 'Enable', 'off')
set(handles.btnPlot1, 'Enable', 'on')
set(handles.btnPlot3, 'Enable', 'on')
set(handles.btnPlot4, 'Enable', 'on')
set(handles.btnPlot5, 'Enable', 'on')
set(handles.btnClear, 'Enable', 'on')

set(handles.rbMarkCirc, 'Enable', 'on')
set(handles.rbMarkSq, 'Enable', 'on')
set(handles.rbMarkNone, 'Enable', 'on')
set(handles.rbMarkStar, 'Enable', 'on')
set(handles.rbMarkTriangle, 'Enable', 'on')
set(handles.rbMarkRhombus, 'Enable', 'on')

set(handles.pmColor, 'Enable', 'on')
set(handles.scrWidth, 'Enable', 'on')

if get(handles.chbxGridX, 'Value')
    set(gca,'XGrid', 'on')
else
    set(gca,'XGrid','off')
end
if get(handles.chbxGridY, 'Value')
    set(gca,'YGrid', 'on')
else
    set(gca,'YGrid','off')
end

if get(handles.rbMarkCirc, 'Value')
    set(handles.Line, 'Marker', 'o')
end
if get(handles.rbMarkSq, 'Value')
    set(handles.Line, 'Marker', 's')
end
if get(handles.rbMarkStar, 'Value')
    set(handles.Line, 'Marker', '*')
end
if get(handles.rbMarkTriangle, 'Value')
    set(handles.Line, 'Marker', '^')
end
if get(handles.rbMarkRhombus, 'Value')
    set(handles.Line, 'Marker', 'd')
end

if get(handles.rbMarkCirc, 'Value')
    set(handles.rbMarkCirc, 'Enable', 'inactive')
end
if get(handles.rbMarkSq, 'Value')
    set(handles.rbMarkSq, 'Enable', 'inactive')
end
if get(handles.rbMarkNone, 'Value')
    set(handles.rbMarkNone, 'Enable', 'inactive')
end
if get(handles.rbMarkStar, 'Value')
    set(handles.rbMarkStar, 'Enable', 'inactive')
end
if get(handles.rbMarkTriangle, 'Value')
    set(handles.rbMarkTriangle, 'Enable', 'inactive')
end
if get(handles.rbMarkRhombus, 'Value')
    set(handles.rbMarkRhombus, 'Enable', 'inactive')
end

Num=get(handles.pmColor, 'Value');
switch Num
    case 1
        set(handles.Line, 'Color', 'b')
    case 2
        set(handles.Line, 'Color', 'r')
    case 3
        set(handles.Line, 'Color', 'g')
    case 4
        set(handles.Line, 'Color', 'y')
    case 5
        set(handles.Line, 'Color', 'k')
    case 6
        set(handles.Line, 'Color', 'm')
    case 7
        set(handles.Line, 'Color', 'c')
end


width=get(handles.scrWidth, 'Value');
set(handles.Line, 'LineWidth', round(width))

% --- Executes on button press in btnPlot3.
function btnPlot3_Callback(hObject, eventdata, handles)
% hObject    handle to btnPlot3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
x=-2:0.2:2;
y=exp(-x.^4);
handles.Line=plot(x,y);
guidata(gcbo, handles)

set(hObject, 'Enable', 'off')
set(handles.btnPlot1, 'Enable', 'on')
set(handles.btnPlot2, 'Enable', 'on')
set(handles.btnPlot4, 'Enable', 'on')
set(handles.btnPlot5, 'Enable', 'on')
set(handles.btnClear, 'Enable', 'on')

set(handles.rbMarkCirc, 'Enable', 'on')
set(handles.rbMarkSq, 'Enable', 'on')
set(handles.rbMarkNone, 'Enable', 'on')
set(handles.rbMarkStar, 'Enable', 'on')
set(handles.rbMarkTriangle, 'Enable', 'on')
set(handles.rbMarkRhombus, 'Enable', 'on')

set(handles.pmColor, 'Enable', 'on')
set(handles.scrWidth, 'Enable', 'on')

if get(handles.chbxGridX, 'Value')
    set(gca,'XGrid', 'on')
else
    set(gca,'XGrid','off')
end
if get(handles.chbxGridY, 'Value')
    set(gca,'YGrid', 'on')
else
    set(gca,'YGrid','off')
end


if get(handles.rbMarkCirc, 'Value')
    set(handles.Line, 'Marker', 'o')
end
if get(handles.rbMarkSq, 'Value')
    set(handles.Line, 'Marker', 's')
end
if get(handles.rbMarkStar, 'Value')
    set(handles.Line, 'Marker', '*')
end
if get(handles.rbMarkTriangle, 'Value')
    set(handles.Line, 'Marker', '^')
end
if get(handles.rbMarkRhombus, 'Value')
    set(handles.Line, 'Marker', 'd')
end

if get(handles.rbMarkCirc, 'Value')
    set(handles.rbMarkCirc, 'Enable', 'inactive')
end
if get(handles.rbMarkSq, 'Value')
    set(handles.rbMarkSq, 'Enable', 'inactive')
end
if get(handles.rbMarkNone, 'Value')
    set(handles.rbMarkNone, 'Enable', 'inactive')
end
if get(handles.rbMarkStar, 'Value')
    set(handles.rbMarkStar, 'Enable', 'inactive')
end
if get(handles.rbMarkTriangle, 'Value')
    set(handles.rbMarkTriangle, 'Enable', 'inactive')
end
if get(handles.rbMarkRhombus, 'Value')
    set(handles.rbMarkRhombus, 'Enable', 'inactive')
end

Num=get(handles.pmColor, 'Value');
switch Num
    case 1
        set(handles.Line, 'Color', 'b')
    case 2
        set(handles.Line, 'Color', 'r')
    case 3
        set(handles.Line, 'Color', 'g')
    case 4
        set(handles.Line, 'Color', 'y')
    case 5
        set(handles.Line, 'Color', 'k')
    case 6
        set(handles.Line, 'Color', 'm')
    case 7
        set(handles.Line, 'Color', 'c')
end

width=get(handles.scrWidth, 'Value');
set(handles.Line, 'LineWidth', round(width))


% --- Executes on button press in chbxGridX.
function chbxGridX_Callback(hObject, eventdata, handles)
% hObject    handle to chbxGridX (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of chbxGridX
if get(hObject, 'Value')
    set(gca,'XGrid', 'on')
else
    set(gca,'XGrid','off')
end

% --- Executes on button press in chbxGridY.
function chbxGridY_Callback(hObject, eventdata, handles)
% hObject    handle to chbxGridY (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of chbxGridY
if get(hObject, 'Value')
    set(gca,'YGrid', 'on')
else
    set(gca,'YGrid','off')
end


% --- Executes on button press in rbMarkCirc.
function rbMarkCirc_Callback(hObject, eventdata, handles)
% hObject    handle to rbMarkCirc (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of rbMarkCirc
set(handles.Line, 'Marker', 'o')
set(hObject, 'Enable', 'inactive')
set(handles.rbMarkSq, 'Enable', 'on')
set(handles.rbMarkNone, 'Enable', 'on')
set(handles.rbMarkStar, 'Enable', 'on')
set(handles.rbMarkTriangle, 'Enable', 'on')
set(handles.rbMarkRhombus, 'Enable', 'on')

% --- Executes on button press in rbMarkSq.
function rbMarkSq_Callback(hObject, eventdata, handles)
% hObject    handle to rbMarkSq (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of rbMarkSq
set(handles.Line, 'Marker', 's')
set(hObject, 'Enable', 'inactive')
set(handles.rbMarkCirc, 'Enable', 'on')
set(handles.rbMarkNone, 'Enable', 'on')
set(handles.rbMarkStar, 'Enable', 'on')
set(handles.rbMarkTriangle, 'Enable', 'on')
set(handles.rbMarkRhombus, 'Enable', 'on')


% --- Executes on button press in rbMarkNone.
function rbMarkNone_Callback(hObject, eventdata, handles)
% hObject    handle to rbMarkNone (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of rbMarkNone
set(handles.Line, 'Marker', 'none')
set(hObject, 'Enable', 'inactive')
set(handles.rbMarkCirc, 'Enable', 'on')
set(handles.rbMarkSq, 'Enable', 'on')
set(handles.rbMarkStar, 'Enable', 'on')
set(handles.rbMarkTriangle, 'Enable', 'on')
set(handles.rbMarkRhombus, 'Enable', 'on')


% --- Executes on button press in btnPlot4.
function btnPlot4_Callback(hObject, eventdata, handles)
% hObject    handle to btnPlot4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
x=-2:0.2:2;
y=exp(-x.^5);
handles.Line=plot(x,y)
guidata(gcbo, handles)

set(hObject, 'Enable', 'off')
set(handles.btnPlot1, 'Enable', 'on')
set(handles.btnPlot2, 'Enable', 'on')
set(handles.btnPlot3, 'Enable', 'on')
set(handles.btnPlot5, 'Enable', 'on')
set(handles.btnClear, 'Enable', 'on')

set(handles.rbMarkCirc, 'Enable', 'on')
set(handles.rbMarkSq, 'Enable', 'on')
set(handles.rbMarkNone, 'Enable', 'on')
set(handles.rbMarkStar, 'Enable', 'on')
set(handles.rbMarkTriangle, 'Enable', 'on')
set(handles.rbMarkRhombus, 'Enable', 'on')

set(handles.pmColor, 'Enable', 'on')
set(handles.scrWidth, 'Enable', 'on')

if get(handles.chbxGridX, 'Value')
    set(gca,'XGrid', 'on')
else
    set(gca,'XGrid','off')
end
if get(handles.chbxGridY, 'Value')
    set(gca,'YGrid', 'on')
else
    set(gca,'YGrid','off')
end

if get(handles.rbMarkCirc, 'Value')
    set(handles.Line, 'Marker', 'o')
end
if get(handles.rbMarkSq, 'Value')
    set(handles.Line, 'Marker', 's')
end
if get(handles.rbMarkStar, 'Value')
    set(handles.Line, 'Marker', '*')
end
if get(handles.rbMarkTriangle, 'Value')
    set(handles.Line, 'Marker', '^')
end
if get(handles.rbMarkRhombus, 'Value')
    set(handles.Line, 'Marker', 'd')
end

if get(handles.rbMarkCirc, 'Value')
    set(handles.rbMarkCirc, 'Enable', 'inactive')
end
if get(handles.rbMarkSq, 'Value')
    set(handles.rbMarkSq, 'Enable', 'inactive')
end
if get(handles.rbMarkNone, 'Value')
    set(handles.rbMarkNone, 'Enable', 'inactive')
end
if get(handles.rbMarkStar, 'Value')
    set(handles.rbMarkStar, 'Enable', 'inactive')
end
if get(handles.rbMarkTriangle, 'Value')
    set(handles.rbMarkTriangle, 'Enable', 'inactive')
end
if get(handles.rbMarkRhombus, 'Value')
    set(handles.rbMarkRhombus, 'Enable', 'inactive')
end

Num=get(handles.pmColor, 'Value');
switch Num
    case 1
        set(handles.Line, 'Color', 'b')
    case 2
        set(handles.Line, 'Color', 'r')
    case 3
        set(handles.Line, 'Color', 'g')
    case 4
        set(handles.Line, 'Color', 'y')
    case 5
        set(handles.Line, 'Color', 'k')
    case 6
        set(handles.Line, 'Color', 'm')
    case 7
        set(handles.Line, 'Color', 'c')
end

width=get(handles.scrWidth, 'Value');
set(handles.Line, 'LineWidth', round(width))


% --- Executes on button press in btnPlot5.
function btnPlot5_Callback(hObject, eventdata, handles)
% hObject    handle to btnPlot5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
x=-2:0.2:2;
y=exp(-x.^6);
handles.Line=plot(x,y)
guidata(gcbo, handles)

set(hObject, 'Enable', 'off')
set(handles.btnPlot1, 'Enable', 'on')
set(handles.btnPlot2, 'Enable', 'on')
set(handles.btnPlot3, 'Enable', 'on')
set(handles.btnPlot4, 'Enable', 'on')
set(handles.btnClear, 'Enable', 'on')

set(handles.rbMarkCirc, 'Enable', 'on')
set(handles.rbMarkSq, 'Enable', 'on')
set(handles.rbMarkNone, 'Enable', 'on')
set(handles.rbMarkStar, 'Enable', 'on')
set(handles.rbMarkTriangle, 'Enable', 'on')
set(handles.rbMarkRhombus, 'Enable', 'on')

set(handles.pmColor, 'Enable', 'on')
set(handles.scrWidth, 'Enable', 'on')

if get(handles.chbxGridX, 'Value')
    set(gca,'XGrid', 'on')
else
    set(gca,'XGrid','off')
end
if get(handles.chbxGridY, 'Value')
    set(gca,'YGrid', 'on')
else
    set(gca,'YGrid','off')
end

if get(handles.rbMarkCirc, 'Value')
    set(handles.Line, 'Marker', 'o')
end
if get(handles.rbMarkSq, 'Value')
    set(handles.Line, 'Marker', 's')
end
if get(handles.rbMarkStar, 'Value')
    set(handles.Line, 'Marker', '*')
end
if get(handles.rbMarkTriangle, 'Value')
    set(handles.Line, 'Marker', '^')
end
if get(handles.rbMarkRhombus, 'Value')
    set(handles.Line, 'Marker', 'd')
end

if get(handles.rbMarkCirc, 'Value')
    set(handles.rbMarkCirc, 'Enable', 'inactive')
end
if get(handles.rbMarkSq, 'Value')
    set(handles.rbMarkSq, 'Enable', 'inactive')
end
if get(handles.rbMarkNone, 'Value')
    set(handles.rbMarkNone, 'Enable', 'inactive')
end
if get(handles.rbMarkStar, 'Value')
    set(handles.rbMarkStar, 'Enable', 'inactive')
end
if get(handles.rbMarkTriangle, 'Value')
    set(handles.rbMarkTriangle, 'Enable', 'inactive')
end
if get(handles.rbMarkRhombus, 'Value')
    set(handles.rbMarkRhombus, 'Enable', 'inactive')
end

Num=get(handles.pmColor, 'Value');
switch Num
    case 1
        set(handles.Line, 'Color', 'b')
    case 2
        set(handles.Line, 'Color', 'r')
    case 3
        set(handles.Line, 'Color', 'g')
    case 4
        set(handles.Line, 'Color', 'y')
    case 5
        set(handles.Line, 'Color', 'k')
    case 6
        set(handles.Line, 'Color', 'm')
    case 7
        set(handles.Line, 'Color', 'c')
end

width=get(handles.scrWidth, 'Value');
set(handles.Line, 'LineWidth', round(width))


% --- Executes on button press in rbMarkStar.
function rbMarkStar_Callback(hObject, eventdata, handles)
% hObject    handle to rbMarkStar (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of rbMarkStar
set(handles.Line, 'Marker', '*')
set(hObject, 'Enable', 'inactive')
set(handles.rbMarkCirc, 'Enable', 'on')
set(handles.rbMarkSq, 'Enable', 'on')
set(handles.rbMarkNone, 'Enable', 'on')
set(handles.rbMarkTriangle, 'Enable', 'on')
set(handles.rbMarkRhombus, 'Enable', 'on')


% --- Executes on button press in rbMarkTriangle.
function rbMarkTriangle_Callback(hObject, eventdata, handles)
% hObject    handle to rbMarkTriangle (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of rbMarkTriangle
set(handles.Line, 'Marker', '^')
set(hObject, 'Enable', 'inactive')
set(handles.rbMarkCirc, 'Enable', 'on')
set(handles.rbMarkSq, 'Enable', 'on')
set(handles.rbMarkNone, 'Enable', 'on')
set(handles.rbMarkStar, 'Enable', 'on')
set(handles.rbMarkRhombus, 'Enable', 'on')


% --- Executes on button press in rbMarkRhombus.
function rbMarkRhombus_Callback(hObject, eventdata, handles)
% hObject    handle to rbMarkRhombus (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of rbMarkRhombus
set(handles.Line, 'Marker', 'd')
set(hObject, 'Enable', 'inactive')
set(handles.rbMarkCirc, 'Enable', 'on')
set(handles.rbMarkSq, 'Enable', 'on')
set(handles.rbMarkNone, 'Enable', 'on')
set(handles.rbMarkStar, 'Enable', 'on')
set(handles.rbMarkTriangle, 'Enable', 'on')


% --- Executes on selection change in pmColor.
function pmColor_Callback(hObject, eventdata, handles)
% hObject    handle to pmColor (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns pmColor contents as cell array
%        contents{get(hObject,'Value')} returns selected item from pmColor
Num=get(hObject, 'Value');
switch Num
    case 1
        set(handles.Line, 'Color', 'b')
    case 2
        set(handles.Line, 'Color', 'r')
    case 3
        set(handles.Line, 'Color', 'g')
    case 4
        set(handles.Line, 'Color', 'y')
    case 5
        set(handles.Line, 'Color', 'k')
    case 6
        set(handles.Line, 'Color', 'm')
    case 7
        set(handles.Line, 'Color', 'c')
end

% --- Executes during object creation, after setting all properties.
function pmColor_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pmColor (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on slider movement.
function scrWidth_Callback(hObject, eventdata, handles)
% hObject    handle to scrWidth (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
width=get(hObject, 'Value');
set(handles.Line, 'LineWidth', round(width))

% --- Executes during object creation, after setting all properties.
function scrWidth_CreateFcn(hObject, eventdata, handles)
% hObject    handle to scrWidth (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end
