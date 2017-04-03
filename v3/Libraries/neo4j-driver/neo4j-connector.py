#!/usr/bin/env python
# -*- coding: utf8 -*-


from neo4j.v1 import GraphDatabase, basic_auth

# Neo4j Configuration
neo4j_server = '10.100.0.107'
neo4j_server_port = '31821'
# neo4j_server = '192.168.99.100'
# neo4j_server_port = '31895'
neo4j_bolt_connection = 'bolt://{}:{}'.format(neo4j_server, neo4j_server_port)
user = input('User (default: neo4j): ') or 'neo4j'
password = input('Password for {}: '.format(user)) or 'portal'

# Neo4j Database Connection
driver = GraphDatabase.driver(neo4j_bolt_connection, auth=basic_auth(user, password))


def create_node():
    """Create Neo4j Nodes"""

    session = driver.session()
    session.run(
        "CREATE (a:Person {name: 'Arthur', title: 'King'})"
    )
    session.close()


def search():
    """Search Neo4j Database"""

    session = driver.session()
    result = session.run(
        "match (n) "
        "return n, n.name as name, n.title as title"
    )

    for record in result:
        print(record)

    session.close()


def drop():
    """Drop all nodes"""

    if input('Deleting everything, are you sure? Type "Yes I\'m sure": ') in "Yes I\'m sure":

        try:
            session = driver.session()
            session.run("match (n) detach delete n")
            session.close()
            print('[*] Deleted.')

        except:
            raise

    else:
        print('[*] Nothing deleted.')


# Main
if __name__ == "__main__":
    # create_node()
    # search()
    drop()
    pass
