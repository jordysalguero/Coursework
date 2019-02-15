Attribute VB_Name = "Module1"
Sub EasyStockData()

'Calling each worksheet in the excel file'

For Each ws In Worksheets

'Declaring each variable'

    Dim tickerbrand As String
    Dim tickercolumn As Integer
    Dim tickervolumecolumn As Integer
    Dim tickervolumesummary As Double
    Dim summaryrow As Double
    Dim i As Double
    Dim lastrow As Long
    Dim worksheetname As String
    
'Provided the values to the variables'

    worksheetname = ws.Name
    tickercolumn = 1
    tickertotalvolume = 0
    tickervolumecolumn = 7
    summaryrow = 2
    lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    
    
'Started my loop'

        For i = 2 To lastrow
            
'Checking if the values in the first cell matches the second'

            If ws.Cells(i + 1, tickercolumn).Value <> ws.Cells(i, tickercolumn).Value Then
            
'Declaring the values on the dataset along with where I want the summary values to appear'

                tickerbrand = ws.Cells(i, tickercolumn).Value
                tickervolumesummary = tickervolumesummary + ws.Cells(i, tickervolumecolumn).Value
                ws.Range("I1").Value = "Ticker"
                ws.Range("J1").Value = "Total Stock Volume"
                ws.Range("I" & summaryrow).Value = tickerbrand
                ws.Range("J" & summaryrow).Value = tickervolumesummary
                
'Adding one to the summary row to move on the next row'

                summaryrow = summaryrow + 1
                
'Resetting the counter'

                tickervolumesummary = 0
                
            Else
            
                tickervolumesummary = tickervolumesummary + ws.Cells(i, tickervolumecolumn).Value
                
'Closing the script'
               
            End If
                
        Next i
        
Next ws
            
End Sub
