import requests
from bs4 import BeautifulSoup

def get_sudoku(p_link, s_link):
    """
    Return a random Sudoku puzzle and solution, given puzzle link and solution
    """
    req = requests.get(p_link)
    c = req.content
    soup = BeautifulSoup(c, 'html.parser')

    grid_txt = soup.find_all('div', {'class':'grid'})[0].text
    puzzle_no = grid_txt[str.find(grid_txt, 'Showing puzzle')+23:str.find(grid_txt, 'Puzzletype')]

    rows = soup.find_all('tr', {'class':'grid'})
    puzzle = []
    for row in rows:
        cols = row.find_all('td')
        for col in cols:
            txt = col.text
            if txt != '\xa0':
                puzzle.append(txt)
            else:
                puzzle.append('0')
    puzzle = ' '.join(puzzle)


    req_sol = requests.get(s_link.format(puzzle_no))
    c = req_sol.content
    soup = BeautifulSoup(c, 'html.parser')
    rows = soup.find_all('tr', {'class':'grid'})
    solution = []
    for row in rows:
        cols = row.find_all('td')
        for col in cols:
            txt = col.text
            if txt != '\xa0':
                solution.append(txt)
            else:
                solution.append('0')
    solution = ' '.join(solution)

    return puzzle, solution
