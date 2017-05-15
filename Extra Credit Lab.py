series1 = []
series2 = []
series3 = []
series4 = []
series5 = []


for currentSeries in range(1, 6):
    print("Currently editing series", currentSeries)
    try:
        seriesEdit = list(input("Put numbers in ").split(' '))
        #   seriesEdit = input("Enter the numbers you want to add to the series seperated by a space. ").split(' ')
    except NameError:
        print("Please enter a correct value.")

    #   http://stackoverflow.com/questions/23375606/converting-list-items-from-string-to-intpython
    for i in range(len(seriesEdit)):
        try:
            seriesEdit[i] = int(seriesEdit[i])
        except ValueError:
            print("You enter nothing. Thats weird...")
            pass

    if currentSeries == 1:
        series1.append(seriesEdit)
    if currentSeries == 2:
        series2.append(seriesEdit)
    if currentSeries == 3:
        series3.append(seriesEdit)
    if currentSeries == 4:
        series4.append(seriesEdit)
    if currentSeries == 5:
        series5.append(seriesEdit)

print("Series 1: ", series1)
print("Series 2: ", series2)
print("Series 3: ", series3)
print("Series 4: ", series4)
print("Series 5: ", series5)
