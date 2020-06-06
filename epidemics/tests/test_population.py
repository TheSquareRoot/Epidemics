from unittest import TestCase
import epidemics.population.population as population


class TestPopulation(TestCase):
    def test_generate(self):
        pass

    def test_random_agent(self):
        habitants, agents = [], {}
        p = population.Population(habitants, agents)
        uid, agent = p.random_agent(0, 10, 0)
        self.assertTrue(agent['age'] <= 10)
        self.assertEqual(agent['prevposition'], 0)
        self.assertEqual(agent['position'], 0)
        self.assertEqual(agent['state'], 1)
