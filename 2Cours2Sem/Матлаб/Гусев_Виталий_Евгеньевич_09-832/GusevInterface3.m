function varargout = GusevInterface3(varargin)
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @GusevInterface3_OpeningFcn, ...
                   'gui_OutputFcn',  @GusevInterface3_OutputFcn, ...
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

function GusevInterface3_OpeningFcn(hObject, eventdata, handles, varargin)
handles.output = hObject;

guidata(hObject, handles);



function varargout = GusevInterface3_OutputFcn(hObject, eventdata, handles)
varargout{1} = handles.output;


function btnPlot1_Callback(hObject, eventdata, handles)
x=-5:0.2:5;
y=cos(x);
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

function btnPlot2_Callback(hObject, eventdata, handles)
x=-5:0.2:5;
y=cos(2*x);
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


function btnPlot3_Callback(hObject, eventdata, handles)
x=-5:0.2:5;
y=cos(3*x);
handles.Line=plot(x,y)
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


function btnPlot4_Callback(hObject, eventdata, handles)
x=-5:0.2:5;
y=cos(4*x);
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


function btnPlot5_Callback(hObject, eventdata, handles)
x=-5:0.2:5;
y=cos(5*x);
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


function btnClear_Callback(hObject, eventdata, handles)
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


function chbxGridX_Callback(hObject, eventdata, handles)
if get(hObject, 'Value')
    set(gca,'XGrid', 'on')
else
    set(gca,'XGrid','off')
end


function chbxGridY_Callback(hObject, eventdata, handles)
if get(hObject, 'Value')
    set(gca,'YGrid', 'on')
else
    set(gca,'YGrid','off')
end


function rbMarkCirc_Callback(hObject, eventdata, handles)
set(handles.Line, 'Marker', 'o')
set(hObject, 'Enable', 'inactive')
set(handles.rbMarkSq, 'Enable', 'on')
set(handles.rbMarkNone, 'Enable', 'on')
set(handles.rbMarkStar, 'Enable', 'on')
set(handles.rbMarkTriangle, 'Enable', 'on')
set(handles.rbMarkRhombus, 'Enable', 'on')


function rbMarkStar_Callback(hObject, eventdata, handles)
set(handles.Line, 'Marker', '*')
set(hObject, 'Enable', 'inactive')
set(handles.rbMarkCirc, 'Enable', 'on')
set(handles.rbMarkSq, 'Enable', 'on')
set(handles.rbMarkNone, 'Enable', 'on')
set(handles.rbMarkTriangle, 'Enable', 'on')
set(handles.rbMarkRhombus, 'Enable', 'on')


function rbMarkTriangle_Callback(hObject, eventdata, handles)
set(handles.Line, 'Marker', '^')
set(hObject, 'Enable', 'inactive')
set(handles.rbMarkCirc, 'Enable', 'on')
set(handles.rbMarkSq, 'Enable', 'on')
set(handles.rbMarkNone, 'Enable', 'on')
set(handles.rbMarkStar, 'Enable', 'on')
set(handles.rbMarkRhombus, 'Enable', 'on')


function rbMarkRhombus_Callback(hObject, eventdata, handles)
set(handles.Line, 'Marker', 'd')
set(hObject, 'Enable', 'inactive')
set(handles.rbMarkCirc, 'Enable', 'on')
set(handles.rbMarkSq, 'Enable', 'on')
set(handles.rbMarkNone, 'Enable', 'on')
set(handles.rbMarkStar, 'Enable', 'on')
set(handles.rbMarkTriangle, 'Enable', 'on')


function rbMarkSq_Callback(hObject, eventdata, handles)
set(handles.Line, 'Marker', 's')
set(hObject, 'Enable', 'inactive')
set(handles.rbMarkCirc, 'Enable', 'on')
set(handles.rbMarkNone, 'Enable', 'on')
set(handles.rbMarkStar, 'Enable', 'on')
set(handles.rbMarkTriangle, 'Enable', 'on')
set(handles.rbMarkRhombus, 'Enable', 'on')


function rbMarkNone_Callback(hObject, eventdata, handles)
set(handles.Line, 'Marker', 'none')
set(hObject, 'Enable', 'inactive')
set(handles.rbMarkCirc, 'Enable', 'on')
set(handles.rbMarkSq, 'Enable', 'on')
set(handles.rbMarkStar, 'Enable', 'on')
set(handles.rbMarkTriangle, 'Enable', 'on')
set(handles.rbMarkRhombus, 'Enable', 'on')


function pmColor_Callback(hObject, eventdata, handles)
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


function pmColor_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


function scrWidth_Callback(hObject, eventdata, handles)
width=get(hObject, 'Value');
set(handles.Line, 'LineWidth', round(width))


function scrWidth_CreateFcn(hObject, eventdata, handles)
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end
