package main

import (
	"sort"
	"strconv"
	"strings"
)

type Material struct {
	material string
	type_    string
}

func (m *Material) str() string {
	return m.material + m.type_
}

func NewMicrochip(material string) *Material {
	return &Material{material, "M"}
}

func NewGenerator(material string) *Material {
	return &Material{material, "G"}
}

type Floor struct {
	microchips *Set[Material]
	generators *Set[Material]
}

func (f *Floor) get_all() *Set[Material] {
	return f.microchips.union(f.generators)
}

func (f *Floor) pop(material Material) {
	if material.type_ == "M" {
		f.microchips.remove(material)
	} else if material.type_ == "G" {
		f.generators.remove(material)
	}
}

func (f *Floor) push(material Material) {
	if material.type_ == "M" {
		f.microchips.add(material)
	} else if material.type_ == "G" {
		f.generators.add(material)
	}
}

func (f *Floor) len() int {
	return f.microchips.len() + f.generators.len()
}

func (f *Floor) str() string {
	chips := f.microchips.list_of_elements()
	str_chips := []string{}
	for _, chip := range chips {
		str_chips = append(str_chips, chip.str())
	}
	sort.Strings(str_chips)
	chips_repr := strings.Join(str_chips, ",")

	gens := f.generators.list_of_elements()
	str_gens := []string{}
	for _, gen := range gens {
		str_gens = append(str_gens, gen.str())
	}
	sort.Strings(str_gens)
	gens_repr := strings.Join(str_gens, ",")

	return chips_repr + "," + gens_repr
}

func NewFloor(microchips *Set[Material], generators *Set[Material]) *Floor {
	return &Floor{microchips, generators}
}

type Building struct {
	current_floor int
	floors        []*Floor
	length        int
}

func (b *Building) str() string {
	cf := strconv.Itoa(b.current_floor)
	length_ := strconv.Itoa(b.length)

	floors_ := []string{}
	for n, floor := range b.floors {
		floors_ = append(floors_, strconv.Itoa(n)+":")
		floors_ = append(floors_, floor.str())
	}
	floors_repr := strings.Join(floors_, "")

	return cf + "/" + length_ + "/" + floors_repr
}

func (b *Building) hash() string {
	item_pair := make(map[string][]int)

	for i, floor := range b.floors {
		for _, chip := range floor.microchips.list_of_elements() {
			item_pair[chip.material] = []int{i}
		}
	}

	for i, floor := range b.floors {
		for _, gen := range floor.generators.list_of_elements() {
			item_pair[gen.material] = append(item_pair[gen.material], i)
		}
	}

	output := []string{}
	for _, v := range item_pair {
		single := []string{}
		for _, i := range v {
			single = append(single, strconv.Itoa(i))
		}
		output = append(output, "["+strings.Join(single, ",")+"]")
	}
	sort.Strings(output)
	output_str := strings.Join(output, "")
	output_str = "[" + output_str + "]"

	return output_str + strconv.Itoa(b.current_floor)
}

func (b *Building) is_radiation_ok() bool {
	for floor := 0; floor < b.length; floor++ {

		generators := make(map[string]bool)
		for g := range b.floors[floor].generators.elements {
			generators[g.material] = true
		}

		microchips := []string{}
		for m := range b.floors[floor].microchips.elements {
			microchips = append(microchips, m.material)
		}

		if len(generators) == 0 {
			continue
		}

		for _, microchip := range microchips {
			_, corresponding_generator_is_there := generators[microchip]
			if !corresponding_generator_is_there {
				return false
			}
		}
	}
	return true
}

func (b *Building) all_on_4th() bool {
	for floor := range b.length - 1 {
		if b.floors[floor].len() > 0 {
			return false
		}
	}
	return true
}

func (b *Building) next_states() []*Building {

	output_states := []*Building{}

	for _, next_floor := range []int{b.current_floor - 1, b.current_floor + 1} {

		if next_floor < 0 || next_floor >= b.length {
			continue
		}

		all_elements := b.floors[b.current_floor].get_all().list_of_elements()
		element_selection := [][]Material{}
		for _, e := range all_elements {
			element_selection = append(element_selection, []Material{e})
		}

		for i := range len(all_elements) {
			for j := i + 1; j < len(all_elements); j++ {
				element_selection = append(
					element_selection, []Material{all_elements[i], all_elements[j]},
				)
			}
		}

		for _, elements := range element_selection {
			next_floors := []*Floor{}
			for _, floor := range b.floors {
				next_floors = append(
					next_floors,
					NewFloor(floor.microchips.copy(), floor.generators.copy()),
				)
			}

			for _, element := range elements {
				next_floors[b.current_floor].pop(element)
				next_floors[next_floor].push(element)
			}

			output_states = append(output_states, &Building{next_floor, next_floors, b.length})
		}
	}
	return output_states
}
