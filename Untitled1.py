{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOIfOnhSlrJnpqYeZUSsVik",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jiyeon0325/algorithm_study/blob/main/Untitled1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "sQo3dsHuq55X",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 256
        },
        "outputId": "5624997f-774d-4228-9d04-a47401dc7412"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "26\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-3-bcad97b6ddb2>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      7\u001b[0m     \u001b[0mnum\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m&\u001b[0m\u001b[0;36m10\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0ma\u001b[0m\u001b[0;34m//\u001b[0m\u001b[0;36m10\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m&\u001b[0m\u001b[0;36m10\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m&\u001b[0m\u001b[0;36m10\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0ma\u001b[0m\u001b[0;34m//\u001b[0m\u001b[0;36m10\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m//\u001b[0m\u001b[0;36m10\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m     \u001b[0mcount\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m     \u001b[0;32mif\u001b[0m \u001b[0mnum\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0maint\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0ma\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0maint\u001b[0m \u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     10\u001b[0m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcount\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m         \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ],
      "source": [
        "aint = int(input(\"\"))\n",
        "(0<= aint <= 99)\n",
        "num = aint\n",
        "count = 0\n",
        "while True :\n",
        "    a = num&10 + num//10\n",
        "    num = (a&10 + a//10)&10 + (a&10 + a//10)//10\n",
        "    count += 1\n",
        "    if num == aint or a == aint :\n",
        "        print(count)\n",
        "        break\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "wnYiAXjsbOUL"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}