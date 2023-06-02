import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) {
		InputReader in = new InputReader();
		StringBuilder out = new StringBuilder();

		int T = in.nextInt();
		while (T-- > 0) {
			int a = in.nextInt();
			int b = in.nextInt();
			out.append(a + b).append('\n');
		}

		System.out.print(out);
	}

	static class InputReader {
		public BufferedReader reader;
		public StringTokenizer st;

		public InputReader() {
			reader = new BufferedReader(new InputStreamReader(System.in));
		}

		public String next() {
			while (st == null || !st.hasMoreTokens()) {
				st = new StringTokenizer(nextLine());
			}
			return st.nextToken();
		}

		public String nextLine() {
			try {
				return reader.readLine();
			} catch (IOException e) {
				e.printStackTrace();
			}
			return null;
		}

		public int nextInt() {
			return Integer.parseInt(next());
		}
	}
}