from livereload import Server, shell

if __name__ == '__main__':
    server = Server()
    server.watch('index.html')
    server.serve(root='.')
