Attribute VB_Name = "Module1"
Sub EasyStockData()

For Each ws In Worksheets

    Dim tickerbrand As String
    Dim tickercolumn As Integer
    Dim tickervolumecolumn As Integer
    Dim tickervolumesummary As Double
    Dim summaryrow As Double
    Dim i As Double
    Dim lastrow As Long
    Dim worksheetname As String
    
    worksheetname = ws.Name
    tickercolumn = 1
    tickertotalvolume = 0
    tickervolumecolumn = 7
    summaryrow = 2
    lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    
        For i = 2 To lastrow
            
            If ws.Cells(i + 1, tickercolumn).Value <> ws.Cells(i, tickercolumn).Value Then
            
                tickerbrand = ws.Cells(i, tickercolumn).Value
                tickervolumesummary = tickervolumesummary + ws.Cells(i, tickervolumecolumn).Value
                ws.Range("I1").Value = "Ticker"
                ws.Range("J1").Value = "Total Stock Volume"
                ws.Range("I" & summaryrow).Value = tickerbrand
                ws.Range("J" & summaryrow).Value = tickervolumesummary
                summaryrow = summaryrow + 1
                tickervolumesummary = 0
                
            Else
            
                tickervolumesummary = tickervolumesummary + ws.Cells(i, tickervolumecolumn).Value
                
            End If
                
        Next i
        
Next ws
            
End Sub
