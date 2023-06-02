{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN+rmQAiVd2JmM4KK7iuU59",
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
        "<a href=\"https://colab.research.google.com/github/thiagosilvabarbosa/logica/blob/main/Aula_Listas.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Aula 07 - Listas**"
      ],
      "metadata": {
        "id": "fj05Uwol7596"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Exemplo 1"
      ],
      "metadata": {
        "id": "j1CFrH_P8C1b"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "numeros = []  # cria uma lista vazia\n",
        "num = int(input())  # pede um numero para o laço de repetição\n",
        "\n",
        "for i in range (num):  # cria um laço de repetição com o numero informado\n",
        "    x = int(input())  # pede um número para adiciona-lo a lista\n",
        "    numeros.append(x) # append adiciona o numero pedido a lista numeros\n",
        "\n",
        "for e in numeros:\n",
        "  print(e, end=\"\") # printa a quantidade de números que contem na lista\n",
        "\n",
        "num = int(input())  # pede um novo numero para adicionar o valor a algum indice da lista\n",
        "numeros[2]= num # pega o numero informado e adiciona ao indice [2] da lista\n",
        "for e in numeros: \n",
        "  print(e,end=\"\") # printa novamente a quantidade de número que contém na lista\n"
      ],
      "metadata": {
        "id": "7OT_3Kkb9r8X"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Exemplo 2"
      ],
      "metadata": {
        "id": "v3----q-EOV7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "numeros = []\n",
        "\n",
        "for i in range(5):\n",
        "  numeros.append(int(input()))\n",
        "\n",
        "soma = 0\n",
        "for i in range(5):\n",
        "  soma = soma + numeros[i]\n",
        "print(soma)\n",
        "\n",
        "soma = 0\n",
        "for e in numeros:\n",
        "  soma = soma + e\n",
        "print(soma)\n",
        "\n",
        "media = soma/5\n",
        "print(media)\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kr-7TAp1EOGH",
        "outputId": "c6f99fa0-5a0f-4ec9-f686-0af188673b36"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "2\n",
            "5\n",
            "10\n",
            "10\n",
            "29\n",
            "29\n",
            "5.8\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Parte 2**"
      ],
      "metadata": {
        "id": "2YqtG48HOx8N"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "numeros = [12, 9, 5]\n",
        "len(numeros)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FhOFuTiXOxo0",
        "outputId": "51dfaa79-af63-4286-b047-62f6172ef037"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numeros = [1,2,3,4]\n",
        "numeros.append(8) #adiciona um novo valor a lista\n",
        "for e in numeros:\n",
        "  print(e)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CoKdVw5MPGIO",
        "outputId": "c5f2cdfb-7e99-44b7-f256-9d1e5b91a67d"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numeros = [1,2,3,4]\n",
        "numeros.insert(2,666) #lista.insert(x,y), x é o local da lista e o y é o valor adicionado\n",
        "for e in numeros:\n",
        "  print(e)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "18CAUAcIPwVI",
        "outputId": "16c9efc4-85af-4c0e-8054-b0abddb90c7c"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "666\n",
            "3\n",
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numerosList = []\n",
        "num = int(input())\n",
        "\n",
        "while num >= 0:\n",
        "      numerosList.append(num) \n",
        "      num = int(input())\n",
        "\n",
        "print (f\"{sum(numerosList)/len(numerosList)}\")\n",
        "     \n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bBTsqYe4Qcrw",
        "outputId": "920ce9c8-abf4-4932-cf28-f48522b5f721"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7\n",
            "10\n",
            "-1\n",
            "8.5\n"
          ]
        }
      ]
    }
  ]
}