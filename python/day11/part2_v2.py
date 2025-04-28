import json
import re
from collections import deque
from copy import deepcopy
from queue import PriorityQueue
from typing import Any, Deque, Dict, Generator, List, Set, Tuple


class Material:
    def __init__(self, material: str) -> None:
        self.material: str = material
        self.type: str = ""

    def __repr__(self) -> str:
        return f"{self.material[0].upper()}{self.type}"

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def __eq__(self, other: object) -> Any:
        return str(self) == str(other)

    def __lt__(self, other: object) -> bool:
        return str(self) < str(other)


class Microchip(Material):
    def __init__(self, material: str) -> None:
        super().__init__(material)
        self.type = "M"


class Generator_(Material):
    def __init__(self, material: str) -> None:
        super().__init__(material)
        self.type = "G"


class Floor:
    def __init__(self, microchips: Set[Microchip], generators: Set[Generator_]) -> None:
        self.microchips: Set[Microchip] = microchips
        self.generators: Set[Generator_] = generators

    def get_all(self) -> Set[Material]:
        return self.microchips | self.generators

    def pop(self, material: Material) -> None:
        if isinstance(material, Microchip):
            self.microchips.remove(material)
        elif isinstance(material, Generator_):
            self.generators.remove(material)

    def push(self, material: Material) -> None:
        if isinstance(material, Microchip):
            self.microchips.add(material)
        elif isinstance(material, Generator_):
            self.generators.add(material)

    def len(self) -> int:
        return len(self.microchips) + len(self.generators)


class Building:
    def __init__(self, current_floor: int, floors: List[Floor]) -> None:
        self.current_floor: int = current_floor
        self.floors: List[Floor] = floors
        self.len: int = len(floors)

    def __repr__(self) -> str:
        output: List[str] = []

        for floor in range(self.len - 1, -1, -1):
            floor_output: List[str] = []
            floor_output.append(f"F{floor + 1}")
            if floor == self.current_floor:
                floor_output.append("E")
            else:
                floor_output.append(" ")

            for element in self.floors[floor].get_all():
                floor_output.append(f"{element}")

            output.append(" ".join(floor_output))

        output.append("----")
        return "\n".join(output)

    def repr(self, title: str) -> str:
        output: List[str] = [title]

        for floor in range(self.len - 1, -1, -1):
            floor_output: List[str] = []
            floor_output.append(f"F{floor + 1}")
            if floor == self.current_floor:
                floor_output.append("E")
            else:
                floor_output.append(" ")

            for element in self.floors[floor].get_all():
                floor_output.append(f"{element}")

            output.append(" ".join(floor_output))

        output.append("----")
        return "\n".join(output)

    # def __hash__(self) -> int:
    #     serializable_building: Dict[int | str, int | List[str]] = {
    #         "floor": self.current_floor
    #     }
    #     for floor in range(self.len):
    #         serializable_building[floor] = sorted(
    #             [str(e) for e in self.floors[floor].get_all()]
    #         )

    #     return hash(json.dumps(serializable_building))


    def __hash__(self):
        item_pair = {}
        for i, floor in enumerate(self.floors):
            for chip in floor.microchips:
                item_pair[chip.material] = [i]
        for i, floor in enumerate(self.floors):
            for gen in floor.generators:
                item_pair[gen.material].append(i)
        return hash(str(sorted(item_pair.values())) + str(self.current_floor))


    def __eq__(self, other: object) -> Any:
        return hash(self) == hash(other)

    def is_radiation_ok(self) -> bool:
        for floor in range(self.len):
            generators = [
                str(e)
                for e in self.floors[floor].get_all()
                if isinstance(e, Generator_)
            ]
            microchips = [
                str(e) for e in self.floors[floor].get_all() if isinstance(e, Microchip)
            ]

            if not generators:
                continue

            for microchip in microchips:
                corresponding_generator = microchip[0] + "G"
                if corresponding_generator not in generators:
                    return False

        return True

    def all_on_4th(self) -> bool:
        for floor in range(self.len - 1):
            if self.floors[floor].len() > 0:
                return False
        return True

    def next_states(self) -> Generator[Any, Any, Any]:
        for next_floor in [self.current_floor - 1, self.current_floor + 1]:

            if next_floor < 0 or next_floor >= self.len:
                continue

            all_elements = list(self.floors[self.current_floor].get_all())
            element_selection: List[Tuple[Material] | Tuple[Material, Material]] = [
                (e,) for e in all_elements
            ]
            for i in range(len(all_elements)):
                for j in range(i + 1, len(all_elements)):
                    element_selection.append((all_elements[i], all_elements[j]))

            for elements in element_selection:
                next_floors = deepcopy(self.floors)

                for element in elements:
                    next_floors[self.current_floor].pop(element)
                    next_floors[next_floor].push(element)

                yield Building(next_floor, next_floors)

    def priority(self) -> int:
        return  0
        p: int = 0
        for floor in range(self.len):
            p += self.floors[floor].len() * (2 ** (self.len - 1 - floor))
        return p

    def __lt__(self, other: Any) -> Any:
        return self.priority() < other.priority()


def parse(filename: str) -> Building:
    with open(filename, "r") as fp:
        data: List[str] = fp.read().splitlines()

    microchip_regex: str = r"(\w+)-\w+ microchip"
    gen_regex: str = r"(\w+) generator"

    floors: List[Floor] = []

    for floor, line in enumerate(data):
        microchip_matches: List[str] = re.findall(microchip_regex, line)
        gen_matches: List[str] = re.findall(gen_regex, line)

        microchips: Set[Microchip] = set()
        generators: Set[Generator_] = set()

        for microchip in microchip_matches:
            microchips.add(Microchip(microchip))

        for gen in gen_matches:
            generators.add(Generator_(gen))

        floors.append(Floor(microchips, generators))

    return Building(0, floors)


def solve2(building: Building) -> int:
    # BFS setup
    pqueue: PriorityQueue[Tuple[int, Building]] = PriorityQueue()
    pqueue.put((0, building))
    visited = set([building])

    # BFS
    while pqueue:
        steps, building = pqueue.get()
        # print(building.repr("current building"))

        if building.all_on_4th():
            return steps

        for next_building in building.next_states():
            if next_building not in visited and next_building.is_radiation_ok():
                pqueue.put((steps + 1, next_building))
                visited.add(next_building)

        # break

    return -1

def solve(building: Building) -> int:
    # BFS setup
    queue: Deque[Tuple[int, Building]] = deque([(0, building)])
    visited = set([building])

    # BFS
    while queue:
        steps, building = queue.popleft()

        if building.all_on_4th():
            return steps

        for next_building in building.next_states():
            if next_building not in visited and next_building.is_radiation_ok():
                queue.append((steps + 1, next_building))
                visited.add(next_building)

    return -1



def solution(filename: str) -> int:
    building: Building = parse(filename)

    # floors: List[Floor] = []
    # for _ in range(4):
    #     floors.append(Floor(set(), set()))
    # building: Building = Building(0, floors)

    # Patch building for part 2
    building.floors[0].push(Generator_("elerium"))
    building.floors[0].push(Microchip("elerium"))
    building.floors[0].push(Generator_("dilithium"))
    building.floors[0].push(Microchip("dilithium"))

    return solve(building)


if __name__ == "__main__":
    print(solution("./input.txt"))  # 61
