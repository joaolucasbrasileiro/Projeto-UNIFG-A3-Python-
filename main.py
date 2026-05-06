from app.repositories.vote_repository import VoteRepository


def show_results(title, results):
    print(title)

    for destination, votes in results.items():
        print(f"- {destination}: {votes} voto(s)")

    print()


def main():
    repository = VoteRepository()

    session_name = "Viagem de Ferias"
    destinations = ["Paris", "Roma", "Tokyo"]
    mocked_votes = ["Paris", "Paris", "Roma", "Tokyo", "Paris"]

    repository.create_session_file(session_name, destinations)

    initial_results = repository.read_results(session_name)
    show_results("Resultados iniciais:", initial_results)

    for destination in mocked_votes:
        repository.increement_vote(session_name, destination)

    final_results = repository.read_results(session_name)
    show_results("Resultados depois dos votos mockados:", final_results)


if __name__ == "__main__":
    main()
