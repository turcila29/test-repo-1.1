


# first we create a dictionary with the student's name and results

Romero = {"name": "Romero Chris",
          "homework" : [15],
          "assessment" : [45.50],
          "final exam" : [80]
}

Andreea = {"name": "Andreea Clima",
          "homework" : [25],
          "assessment" : [40],
          "final exam" : [70.20]
}

Jimmy = {"name": "James Umbarto Rafael",
          "homework" : [20],
          "assessment" : [30.80],
          "final exam" : [80]
}

Costache = {"name": " Costache Nea",
          "homework" : [10.10],
          "assessment" : [50],
          "final exam" : [70]
}

#now we create a function that calculates the average

def sum_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)